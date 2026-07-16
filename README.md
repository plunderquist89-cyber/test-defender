# devops-secret-scan-test

Internal test repository for validating **Microsoft Defender for Cloud – DevOps security**
secret scanning coverage (GitHub Advanced Security / Azure DevOps connector).

> **NOTICE:** Every credential, key, token and connection string in this repository is
> **non-functional test data**. None of it authenticates against any real system. It exists
> solely to trigger secret-scanning detections during a controlled test. Do not treat any
> alert generated from this repo as a real exposure.

## What's planted here

| File | Secret type(s) |
|------|----------------|
| `.env` | AWS keys, generic DB password, JWT |
| `src/app.py` | AWS access key + secret |
| `src/database.py` | Postgres connection string w/ password |
| `src/config.js` | Google API key, Slack bot token, Stripe key, SendGrid key, npm token |
| `config/appsettings.json` | Azure AD client secret, Azure Storage connection string |
| `infra/main.tf` | Terraform variable default secret |
| `infra/service-account.json` | GCP service-account private key |
| `keys/deploy_key.pem` | RSA private key |
| `.github/workflows/deploy.yml` | GitHub PAT in workflow |
| `azure-pipelines.yml` | Hardcoded token in pipeline |

## Notes for the test

- Commit **all** files (do not add these to `.gitignore` — they must be tracked to be scanned).
- Pattern-based detections fire on the well-formed fakes below.
- The "verified/active" validity check will mark these **unverified** since they aren't live.
