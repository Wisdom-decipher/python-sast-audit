# Python Flask SAST Audit & Secure Coding Remediation

A static application security testing (SAST) and code review project analyzing a Python Flask authentication service using **Bandit** and manual code inspection against OWASP Top 10 vulnerabilities.

---

## Repository Manifest

| File | Description |
| :--- | :--- |
| `app_before.py` | Baseline vulnerable Flask code containing hardcoded credentials, debug mode, and query syntax defects. |
| `app.py` | Remediated and hardened application enforcing DB-API query parameterization, environment secrets, and secure defaults. |
| `bandit_report_before.txt` | Initial static analysis report documenting baseline vulnerabilities (B106 and B201). |
| `bandit_report_after.txt` | Post-remediation verification report confirming **0** identified security issues. |

---

## Vulnerabilities Identified & Remediations

* **SQL Injection / Parameter Packing Bug (CWE-89):**
  * *Original:* Query string and parameters were packed into a single composite tuple (`query = query_text, params`), breaking driver-level parameter binding.
  * *Fix:* Enforced standard DB-API execution by passing the query template and values as separate arguments: `cursor.execute(query, (username, password))`.

* **Hardcoded Database Credentials (CWE-798 / Bandit B106):**
  * *Original:* Plaintext database password (`rootpass`) stored directly in source code.
  * *Fix:* Externalized sensitive credentials using `os.getenv()`.

* **Interactive Debug Mode Enabled (CWE-94 / Bandit B201):**
  * *Original:* `app.run(debug=True)` exposed the interactive Werkzeug console to arbitrary remote execution.
  * *Fix:* Configured runtime securely with `app.run(debug=False)`.

---

## Static Analysis Verification

```powershell
# Baseline scan
bandit app_before.py -f txt -o bandit_report_before.txt

# Verification re-scan
bandit app.py -f txt -o bandit_report_after.txt
