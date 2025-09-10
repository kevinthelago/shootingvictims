# Shooting Victims Memorial

A Vue.js application that displays a memorial for shooting victims with a respectful fade-in sequence and victim list.

**Live Site:** [shootingvictims.us](https://shootingvictims.us)

## Features

- Memorial screen with fade-in/out "Rest in peace" text
- Counter displaying total number of victims
- List of shooting victims with names and dates
- Non-selectable text throughout the application
- Automated deployment to AWS CloudFront

## Development

### Prerequisites

- Node.js 18+
- npm

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

## Project Structure

```
src/
├── assets/
│   └── victims.json        # Victim data
├── components/
│   └── Person.vue         # Person component
├── App.vue                # Main application component
└── main.js               # Application entry point
```

## Data Format

Victim data in `src/assets/victims.json` follows this structure:

```json
{
  "firstname": "John",
  "lastname": "Doe", 
  "dateOfDeath": "2023-01-15"
}
```