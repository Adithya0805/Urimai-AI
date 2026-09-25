"""Urimai AI — Production Uptime & Latency Monitor
===================================================
Continuous health check and latency monitor for Urimai AI backend & frontend endpoints.
Logs status, response time, database ping, and alerts on degradation.

Usage:
    python scripts/uptime_monitor.py [--target-url http://127.0.0.1:8000] [--interval 30]
"""

import sys
import time
import argparse
import logging
import httpx

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)-7s | %(message)s")
logger = logging.getLogger("urimai.uptime")


def check_health(target_url: str) -> dict:
    health_url = f"{target_url.rstrip('/')}/health"
    start_time = time.time()
    try:
        with httpx.Client(timeout=10.0) as client:
            resp = client.get(health_url)
            elapsed_ms = round((time.time() - start_time) * 1000, 2)

            if resp.status_code == 200:
                data = resp.json()
                logger.info(f"✓ Healthcheck OK: status={resp.status_code} latency={elapsed_ms}ms db={data.get('database')}")
                return {
                    "status": "UP",
                    "status_code": resp.status_code,
                    "latency_ms": elapsed_ms,
                    "database": data.get("database"),
                    "version": data.get("version"),
                }
            else:
                logger.warning(f"⚠️ Healthcheck DEGRADED: status={resp.status_code} latency={elapsed_ms}ms body={resp.text}")
                return {
                    "status": "DEGRADED",
                    "status_code": resp.status_code,
                    "latency_ms": elapsed_ms,
                }
    except Exception as e:
        elapsed_ms = round((time.time() - start_time) * 1000, 2)
        logger.error(f"✗ Healthcheck FAILED: {e} (after {elapsed_ms}ms)")
        return {
            "status": "DOWN",
            "error": str(e),
            "latency_ms": elapsed_ms,
        }


def run_monitor(target_url: str, interval: int = 30, max_iterations: int = 1):
    logger.info(f"Starting Uptime Monitor against {target_url} (interval={interval}s)...")
    iterations = 0
    results = []

    while iterations < max_iterations or max_iterations == 0:
        res = check_health(target_url)
        results.append(res)
        iterations += 1
        if max_iterations != 0 and iterations >= max_iterations:
            break
        time.sleep(interval)

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Urimai AI Uptime Monitor")
    parser.add_argument("--target-url", default="http://127.0.0.1:8000", help="Target base URL")
    parser.add_argument("--interval", type=int, default=30, help="Poll interval in seconds")
    parser.add_argument("--once", action="store_true", help="Run a single check and exit")

    args = parser.parse_args()
    max_iter = 1 if args.once else 0
    run_monitor(args.target_url, args.interval, max_iter)
