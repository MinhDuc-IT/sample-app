const form = document.querySelector("#calculator-form");
const result = document.querySelector("#result");
const error = document.querySelector("#error");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  error.textContent = "";

  const operation = event.submitter.dataset.operation;
  const left = document.querySelector("#left").value;
  const right = document.querySelector("#right").value;

  try {
    const response = await fetch(`/api/${operation}?a=${encodeURIComponent(left)}&b=${encodeURIComponent(right)}`);
    if (!response.ok) throw new Error(`Request failed with HTTP ${response.status}`);
    const payload = await response.json();
    result.textContent = payload.result;
  } catch (requestError) {
    result.textContent = "—";
    error.textContent = requestError.message;
  }
});
