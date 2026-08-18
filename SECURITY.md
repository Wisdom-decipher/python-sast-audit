# Security Policy

## Supported Versions

This repository serves as a static application security testing (SAST) and code review demonstration. Security remediations and patches are actively applied only to the `main` branch.

| Version / Branch | Supported |
| :--------------- | :----------------- |
| `main` (`app.py`) | :white_check_mark: |
| `app_before.py` | :x: (Intentionally Vulnerable Archive) |

---

## Reporting a Vulnerability

If you discover a potential security vulnerability within the remediated codebase or CI/CD pipelines:

1. **Do Not Open a Public Issue:** Please avoid filing public GitHub Issues for newly discovered vulnerabilities to allow for responsible disclosure.
2. **Contact:** Submit a report via GitHub's [Private Vulnerability Reporting](https://github.com/Wisdom-decipher/python-sast-audit/security/advisories/new) feature or contact the maintainer directly.
3. **Report Details:** Include the following information in your report:
   * Description of the vulnerability and its potential impact.
   * Steps to reproduce the issue (proof-of-concept script or payload).
   * Proposed remediation or patch, if available.

---

## Vulnerability Handling Process

* **Acknowledgment:** Initial response and triage within 48 hours.
* **Assessment:** Validation of severity according to CVSS and OWASP guidelines.
* **Remediation:** A fix will be developed, scanned with Bandit SAST, and committed directly to `main`.
