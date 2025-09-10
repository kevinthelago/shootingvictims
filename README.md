# Shooting Victims Memorial

A Vue.js application that displays a memorial for shooting victims with a respectful fade-in sequence and victim list.

**Live Site:** [shootingvictims.us](https://shootingvictims.us)

## Features

- Memorial screen with fade-in/out "Rest in peace" text
- Counter displaying total number of victims
- List of shooting victims with full names and dates
- Non-selectable text throughout the application
- Automated deployment to AWS CloudFront
- Python-based data management tool for adding/removing victims

## Development

### Prerequisites

- Node.js 18+
- npm
- Python 3.6+ (for data management)

### Installation

```bash
npm install
```

### Development Server

```bash
npm run dev
```

### Build

```bash
npm run build
```

## Deployment

The application automatically deploys to AWS CloudFront when code is pushed to the `main` branch.

### Required GitHub Secrets

Configure the following secrets in your GitHub repository settings:

- `AWS_ACCESS_KEY_ID` - AWS access key with S3 and CloudFront permissions
- `AWS_SECRET_ACCESS_KEY` - AWS secret access key
- `AWS_REGION` - AWS region (e.g., `us-east-1`)
- `S3_BUCKET_NAME` - S3 bucket name for hosting the static files
- `CLOUDFRONT_DISTRIBUTION_ID` - CloudFront distribution ID

### AWS Setup

1. Create an S3 bucket configured for static website hosting
2. Create a CloudFront distribution pointing to the S3 bucket
3. Create an IAM user with permissions for S3 and CloudFront operations
4. Add the AWS credentials to GitHub repository secrets

## Data Management

### Python Script (`victims.py`)

A Python script is provided to manage the victim data with duplicate checking and validation.

#### Commands

**Add a new victim:**
```bash
python victims.py add "John" "Michael" "Smith" 25 "2023-05-15"
python victims.py add "Jane" "" "Doe" 30 "2023-06-20"  # No middle name
```

**List all victims:**
```bash
python victims.py list
```

**Remove a victim:**
```bash
python victims.py remove "John" "Michael" "Smith" 25 "2023-05-15"
```

**Get help:**
```bash
python victims.py --help
```

#### Features

- **Duplicate prevention**: Checks all fields (firstname, middlename, lastname, age, dateOfDeath) for uniqueness
- **Date validation**: Ensures dates are in YYYY-MM-DD format
- **Age validation**: Ensures age is a non-negative integer
- **Automatic sorting**: Maintains chronological order (most recent first)
- **Safe operations**: Creates backups and validates JSON structure

## Project Structure

```
├── victims.py              # Python data management script
├── src/
│   ├── assets/
│   │   └── victims.json    # Victim data
│   ├── components/
│   │   └── Victim.vue      # Victim display component
│   ├── App.vue             # Main application component
│   └── main.js            # Application entry point
└── .github/workflows/
    └── deploy.yml          # GitHub Actions deployment
```

## Data Format

Victim data in `src/assets/victims.json` follows this structure:

```json
{
  "firstname": "John",
  "middlename": "Michael",
  "lastname": "Smith",
  "age": 25,
  "dateOfDeath": "2023-01-15"
}
```

**Field descriptions:**
- `firstname` (required): First name of the victim
- `middlename` (optional): Middle name (can be empty string)
- `lastname` (required): Last name of the victim
- `age` (required): Age at time of death (integer ≥ 0)
- `dateOfDeath` (required): Date in YYYY-MM-DD format

**Display format:**
- Full name is displayed as "Firstname Middlename Lastname" (middle name omitted if empty)
- Date is right-aligned
- Age is stored but not displayed in the UI
- List is automatically sorted by date (most recent first)