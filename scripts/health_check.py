import urllib.request
import urllib.error
import json
from datetime import datetime


BASE_URL = "http://localhost:8080"

ENDPOINTS = [
    "/api/books",
    "/api/books/available",
]


def check_endpoint(url: str) -> dict:
    """Check if an endpoint is healthy."""
    try:
        start = datetime.now()
        with urllib.request.urlopen(url, timeout=5) as response:
            elapsed = (datetime.now() - start).total_seconds() * 1000
            return {
                "url": url,
                "status": response.status,
                "healthy": response.status == 200,
                "response_time_ms": round(elapsed, 2)
            }
    except urllib.error.URLError as e:
        return {
            "url": url,
            "status": 0,
            "healthy": False,
            "error": str(e)
        }


def run_health_check():
    """Run health checks on all endpoints."""
    print(f"\nHealth Check Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    results = []
    for endpoint in ENDPOINTS:
        result = check_endpoint(BASE_URL + endpoint)
        results.append(result)

        status = "OK" if result["healthy"] else "FAIL"
        if result["healthy"]:
            print(f"[{status}] {endpoint} — {result['response_time_ms']}ms")
        else:
            print(f"[{status}] {endpoint} — {result.get('error', 'Unknown error')}")

    healthy = sum(1 for r in results if r["healthy"])
    print(f"\nResult: {healthy}/{len(results)} endpoints healthy")

    report = {
        "timestamp": datetime.now().isoformat(),
        "results": results,
        "summary": {
            "total": len(results),
            "healthy": healthy,
            "unhealthy": len(results) - healthy
        }
    }

    with open("scripts/health_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print("Report saved to scripts/health_report.json")


if __name__ == "__main__":
    run_health_check()