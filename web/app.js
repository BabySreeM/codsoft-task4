let pyodide;
let currentCategory = "movies";
let currentAlgo = "content";
let ratings = {
  movies: {},
  books: {},
  products: {},
};

async function initPyodide() {
  pyodide = await loadPyodide({
    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.2/full/",
  });

  // Load recommender.py into Pyodide filesystem
  const resp = await fetch("recommender.py");
  const code = await resp.text();
  pyodide.FS.writeFile("recommender.py", code);
  pyodide.runPython("import recommender");

  document.getElementById("loading").style.display = "none";
  document.getElementById("recommend-btn").disabled = true;

  loadItems();
}

// Get items from DATASETS dict in Python
function getDataset(category) {
  const json = pyodide.runPython(
    `import json, recommender; json.dumps(recommender.DATASETS["${category}"])`
  );
  return JSON.parse(json);
}

function loadItems() {
  const itemsGrid = document.getElementById("items-grid");
  const tagTabs = document.getElementById("tag-tabs");
  itemsGrid.innerHTML = "";
  tagTabs.innerHTML = "";

  const items = getDataset(currentCategory);

  const allTags = Array.from(new Set(items.flatMap((i) => i.tags))).sort();
  const tags = ["All", ...allTags];

  tags.forEach((tag, idx) => {
    const btn = document.createElement("button");
    btn.className = "tag-tab" + (idx === 0 ? " active" : "");
    btn.textContent = tag;
    btn.dataset.tag = tag;
    btn.addEventListener("click", () => {
      document
        .querySelectorAll(".tag-tab")
        .forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      renderItems(items, tag === "All" ? null : tag);
    });
    tagTabs.appendChild(btn);
  });

  renderItems(items, null);
}

function renderItems(items, activeTag) {
  const itemsGrid = document.getElementById("items-grid");
  itemsGrid.innerHTML = "";
  const currentRatings = ratings[currentCategory];

  items
    .filter((it) => !activeTag || it.tags.includes(activeTag))
    .forEach((item) => {
      const card = document.createElement("div");
      card.className = "item-card" + (currentRatings[item.id] ? " rated" : "");

      const info = document.createElement("div");
      info.className = "item-info";

      const title = document.createElement("div");
      title.className = "item-title";
      title.textContent = item.title;

      const sub = document.createElement("div");
      sub.className = "item-sub";
      sub.textContent = `${item.subtitle} · ${item.year}`;

      const tagsDiv = document.createElement("div");
      tagsDiv.className = "item-tags";
      item.tags.forEach((t) => {
        const span = document.createElement("span");
        span.className = "tag";
        span.textContent = t;
        tagsDiv.appendChild(span);
      });

      const stars = document.createElement("div");
      stars.className = "stars";
      [1, 2, 3, 4, 5].forEach((s) => {
        const btn = document.createElement("button");
        btn.className =
          "star" + ((currentRatings[item.id] || 0) >= s ? " filled" : "");
        btn.textContent = "★";
        btn.addEventListener("click", () => {
          rate(item.id, s);
        });
        stars.appendChild(btn);
      });

      info.appendChild(title);
      info.appendChild(sub);
      info.appendChild(tagsDiv);
      info.appendChild(stars);

      card.appendChild(info);
      itemsGrid.appendChild(card);
    });

  updateRatedCount();
  updateRecommendButtonState();
}

function rate(id, score) {
  const currentRatings = ratings[currentCategory];
  if (currentRatings[id] === score) {
    delete currentRatings[id];
  } else {
    currentRatings[id] = score;
  }
  loadItems();
}

function updateRatedCount() {
  const currentRatings = ratings[currentCategory];
  document.getElementById("rated-count").textContent =
    Object.keys(currentRatings).length;
}

function updateRecommendButtonState() {
  const currentRatings = ratings[currentCategory];
  const ratedCount = Object.keys(currentRatings).length;
  const btn = document.getElementById("recommend-btn");
  btn.disabled = ratedCount === 0;
  const hint = document.getElementById("empty-hint");
  hint.style.display = ratedCount === 0 ? "block" : "none";
}

async function recommend() {
  const currentRatings = ratings[currentCategory];
  const ratedCount = Object.keys(currentRatings).length;
  if (!ratedCount) return;

  const btn = document.getElementById("recommend-btn");
  btn.disabled = true;
  const originalLabel = btn.innerHTML;
  btn.innerHTML = '<span class="btn-spinner"></span> Computing…';

  const ratingsDict = {};
  for (const [k, v] of Object.entries(currentRatings)) {
    ratingsDict[parseInt(k, 10)] = v;
  }

  try {
    // Send ratings into Python
    pyodide.globals.set("js_ratings", ratingsDict);

    // DEBUG: see what Python thinks
    const debugJson = pyodide.runPython(`
import json, recommender
json.dumps(recommender.debug_content("${currentCategory}", js_ratings))
`);
    console.log("debug_content:", JSON.parse(debugJson));

    const pythonCode =
      currentAlgo === "content"
        ? `
import json, recommender
json.dumps(recommender.recommend_content("${currentCategory}", js_ratings, 6))
`
        : `
import json, recommender
json.dumps(recommender.recommend_collaborative("${currentCategory}", js_ratings, 6))
`;

    const recsJson = pyodide.runPython(pythonCode);
    const recs = JSON.parse(recsJson);
    renderRecs(recs);
  } catch (err) {
    console.error(err);
    renderRecs([]);
  } finally {
    btn.disabled = false;
    btn.innerHTML = originalLabel;
  }
}

function renderRecs(recs) {
  const list = document.getElementById("recs-list");
  list.innerHTML = "";

  if (!recs || recs.length === 0) {
    const div = document.createElement("div");
    div.className = "empty-hint";
    div.textContent =
      "No recommendations yet. Try rating more items or switching algorithms.";
    list.appendChild(div);
    return;
  }

  recs.forEach((rec, idx) => {
    const card = document.createElement("div");
    card.className = "rec-card";

    const rank = document.createElement("div");
    rank.className = "rec-rank";
    rank.textContent = `#${idx + 1}`;

    const emoji = document.createElement("div");
    emoji.className = "rec-emoji";
    emoji.textContent = rec.emoji;

    const info = document.createElement("div");
    info.className = "rec-info";

    const title = document.createElement("div");
    title.className = "rec-title";
    title.textContent = rec.title;

    const meta = document.createElement("div");
    meta.className = "rec-meta";
    meta.textContent = `${rec.subtitle} · ${rec.year}`;

    const tagsDiv = document.createElement("div");
    tagsDiv.className = "rec-tags";
    rec.tags.forEach((t) => {
      const span = document.createElement("span");
      span.className = "tag";
      span.textContent = t;
      tagsDiv.appendChild(span);
    });

    const reason = document.createElement("div");
    reason.className = "rec-reason";
    reason.textContent = rec.reason;

    info.appendChild(title);
    info.appendChild(meta);
    info.appendChild(tagsDiv);
    info.appendChild(reason);

    const scoreCol = document.createElement("div");
    scoreCol.className = "rec-score-col";

    const barWrap = document.createElement("div");
    barWrap.className = "score-bar-wrap";

    const bar = document.createElement("div");
    bar.className = "score-bar";
    bar.style.width = `${rec.score}%`;

    barWrap.appendChild(bar);

    const label = document.createElement("span");
    label.className = "score-label";
    label.textContent = `${rec.score}%`;

    scoreCol.appendChild(barWrap);
    scoreCol.appendChild(label);

    card.appendChild(rank);
    card.appendChild(emoji);
    card.appendChild(info);
    card.appendChild(scoreCol);

    list.appendChild(card);
  });
}

function setupCategoryTabs() {
  document.querySelectorAll(".cat-tab").forEach((btn) => {
    btn.addEventListener("click", () => {
      document
        .querySelectorAll(".cat-tab")
        .forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      currentCategory = btn.dataset.category;
      loadItems();
    });
  });
}

function setupAlgoButtons() {
  const desc = document.getElementById("algo-desc");
  const note = document.getElementById("algo-note-text");
  document.querySelectorAll(".algo-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document
        .querySelectorAll(".algo-btn")
        .forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      currentAlgo = btn.dataset.algo;
      if (currentAlgo === "content") {
        desc.textContent =
          "Finds items with tags similar to your highly-rated picks.";
        note.innerHTML =
          'Your ratings build a <strong>genre profile</strong>. Python computes <strong>cosine similarity</strong> between that profile and every unrated item to rank suggestions.';
      } else {
        desc.textContent =
          "Matches you with similar users and surfaces what they loved.";
        note.innerHTML =
          'Python uses <strong>user–user cosine similarity</strong> to find simulated users who share your taste, then surfaces what they rated highly.';
      }
    });
  });
}

document
  .getElementById("recommend-btn")
  .addEventListener("click", recommend);

setupCategoryTabs();
setupAlgoButtons();
initPyodide();
