# Production configuration — DO NOT COMMIT
import os

DEBUG = False
SECRET_KEY = "super_secret_key_do_not_share_abc123xyz"

# Database
DATABASE_URL = "postgresql://admin:Passw0rd!123@prod-db.internal:5432/appdb"

# Third-party APIs
STRIPE_API_KEY        = "sk_test_demo_4xKt9mNpQ2rLvWzY8jHdCbEf"
SENDGRID_API_KEY      = "SX.abc123def456.ghiJKLmnoPQRstu"
AWS_ACCESS_KEY_ID     = "DEMO_AKIA_IOSFODNN7EXAMPLEKEY1"
AWS_SECRET_ACCESS_KEY = "DEMO/wJalrXUtnFEMI/K7MDENG/bPxRfiCYKEY"
GITHUB_TOKEN          = "ghx_demo16C7e42F292c6912E7710c838347Ae"
