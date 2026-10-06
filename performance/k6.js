import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: Number(__ENV.VUS || 1),
  duration: __ENV.DURATION || "10s",
  thresholds: {
    http_req_failed: ["rate<0.01"],
    http_req_duration: ["p(95)<500"],
  },
};

export default function () {
  const page = http.get(`${__ENV.BASE_URL}/`);
  check(page, {
    "client page is available": (r) => r.status === 200,
  });

  const response = http.get(`${__ENV.BASE_URL}/api/add?a=2&b=3`);
  check(response, {
    "status is 200": (r) => r.status === 200,
    "result is 5": (r) => r.json().result === 5,
  });
  sleep(1);
}
