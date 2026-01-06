// ADR Fitness - Diet & Workout helper widget
document.addEventListener("DOMContentLoaded", () => {
  const dietEl = document.querySelector(".js-diet-tip");
  const workoutEl = document.querySelector(".js-workout-tip");

  if (dietEl) fetchDietTip(dietEl);
  if (workoutEl) fetchWorkoutTip(workoutEl);
});

async function fetchDietTip(target) {
  target.textContent = "Loading a nutrition tip...";
  try {
    const res = await fetch("https://www.themealdb.com/api/json/v1/1/random.php");
    if (!res.ok) throw new Error("Diet API unavailable");
    const data = await res.json();
    const meal = data?.meals?.[0];
    if (!meal) throw new Error("No meal found");
    const name = meal.strMeal;
    const instructions = meal.strInstructions || "";
    target.innerHTML = `<strong>${name}</strong> — ${truncate(instructions, 180)}`;
  } catch (err) {
    console.error(err);
    target.textContent = pickFallback(dietFallback);
  }
}

async function fetchWorkoutTip(target) {
  target.textContent = "Loading a workout idea...";
  try {
    const res = await fetch("https://wger.de/api/v2/exerciseinfo/?language=2&limit=50");
    if (!res.ok) throw new Error("Workout API unavailable");
    const data = await res.json();
    const results = data?.results || [];
    if (!results.length) throw new Error("No workouts found");
    const item = results[Math.floor(Math.random() * results.length)];
    const name = item.name || "Workout";
    const description = stripHtml(item.description || "");
    target.innerHTML = `<strong>${name}</strong> — ${truncate(description, 170)}`;
  } catch (err) {
    console.error(err);
    target.textContent = pickFallback(workoutFallback);
  }
}

function truncate(text, limit) {
  if (text.length <= limit) return text;
  return `${text.slice(0, limit).trim()}…`;
}

function stripHtml(html) {
  const tmp = document.createElement("div");
  tmp.innerHTML = html;
  return tmp.textContent || tmp.innerText || "";
}

function pickFallback(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

const dietFallback = [
  "Hydrate early: 500ml water within 30 minutes of waking.",
  "Anchor every meal with 30–40g lean protein to support recovery.",
  "Pair carbs with fiber and protein to keep blood sugar stable.",
  "Prioritize whole foods; keep ultra-processed snacks out of sight.",
  "Evening hunger? Add veggies + olive oil to increase fullness."
];

const workoutFallback = [
  "Push-Pull-Legs split: 5x5 compounds, 2–3 accessories, finish with core.",
  "Superset push-ups with inverted rows for efficient upper-body volume.",
  "10-minute finisher: 30s kettlebell swings, 30s rest, repeat x10.",
  "Eccentric control: 3–4s lowering on squats or presses to build strength.",
  "Walk 10 minutes after each meal to aid recovery and digestion."
];
