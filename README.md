# Gambix Website Redesign

A modern, responsive website for Gambix IT Services featuring AI solutions, custom software development, and digital transformation services.

## Features

- **Modern Design**: Dark theme with gradient accents and smooth animations
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive Elements**: Hover effects, scroll animations, and smooth transitions
- **Professional Content**: Comprehensive service offerings and company information
- **Contact Form**: Functional contact form for lead generation

## Pages

- **Home** (`index.html`) - Landing page with hero section and service overview
- **Services** (`services.html`) - Detailed service offerings and features
- **TrueAI** (`tai.html`) - AI solutions and capabilities showcase
- **Projects** (`team.html`) - Team members and project portfolio
- **Contact** (`contact.html`) - Contact information and inquiry form

## Technologies Used

- **HTML5** - Semantic markup
- **CSS3** - Modern styling with CSS Grid, Flexbox, and custom properties
- **JavaScript** - Interactive features and animations
- **Font Awesome** - Icons
- **Google Fonts** - Typography (Manrope and Sora)

## Running Locally

### Option 1: Simple HTTP Server (Recommended)

1. **Clone the repository**:

   ```bash
   git clone <your-repository-url>
   cd gambix_website_redesign
   ```

2. **Start a local server**:

   **Using Python 3**:

   ```bash
   python -m http.server 8000
   ```

   **Using Python 2**:

   ```bash
   python -m SimpleHTTPServer 8000
   ```

   **Using Node.js** (if you have `http-server` installed):

   ```bash
   npx http-server -p 8000
   ```

   **Using PHP**:

   ```bash
   php -S localhost:8000
   ```

3. **Open your browser** and navigate to:
   ```
   http://localhost:8000
   ```

### Option 2: Using FastAPI (Recommended for Development)

1. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI server**:

   ```bash
   python main.py
   ```

3. **Open your browser** and navigate to:

   ```
   http://localhost:8000
   ```

   **Alternative**: Run with uvicorn directly:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Option 3: Using Docker

1. **Build the Docker image**:

   ```bash
   docker build -t gambix-website .
   ```

2. **Run the container**:

   ```bash
   docker run -p 8000:80 gambix-website
   ```

3. **Open your browser** and navigate to:
   ```
   http://localhost:8000
   ```

### Option 4: Direct File Opening

You can also open the HTML files directly in your browser by double-clicking them, but some features (like the contact form) may not work properly due to browser security restrictions.

## Deployment

### AWS App Runner

This project is configured for deployment on AWS App Runner:

1. **Push your code** to a Git repository (GitHub, GitLab, etc.)
2. **Connect your repository** to AWS App Runner
3. **Deploy** using the provided `apprunner.yaml` configuration

The deployment will automatically:

- Install Python dependencies
- Start the FastAPI server
- Serve your static files
- Provide a public URL for your website

### Other Hosting Options

- **GitHub Pages**: Push to a GitHub repository and enable Pages
- **Netlify**: Drag and drop the project folder or connect your Git repository
- **Vercel**: Import your Git repository for automatic deployment
- **AWS S3 + CloudFront**: Upload files to S3 and serve via CloudFront

## Project Structure

```
gambix_website_redesign/
â”œâ”€â”€ index.html          # Home page
â”œâ”€â”€ services.html       # Services page
â”œâ”€â”€ tai.html           # TrueAI page
â”œâ”€â”€ team.html          # Projects/Team page
â”œâ”€â”€ contact.html       # Contact page
â”œâ”€â”€ main.py            # FastAPI server
â”œâ”€â”€ requirements.txt   # Python dependencies
â”œâ”€â”€ apprunner.yaml     # AWS App Runner configuration
â”œâ”€â”€ Dockerfile         # Docker configuration (alternative)
â”œâ”€â”€ nginx.conf         # Nginx configuration (for Docker)
â”œâ”€â”€ .dockerignore      # Docker ignore file
â”œâ”€â”€ .gitignore         # Git ignore file
â””â”€â”€ README.md          # This file
```

## Customization

### Colors

The color scheme is defined using CSS custom properties in the `:root` selector:

- `--primary-color`: #45d0bd (teal)
- `--secondary-color`: #44b6e9 (blue)
- `--dark-bg`: #1f1f1f (dark background)
- `--darker-bg`: #0f0f0f (darker background)

### Fonts

The website uses Google Fonts:

- **Manrope**: Primary body font
- **Sora**: Headings and logo

### Content

Update the HTML files to modify:

- Company information
- Service descriptions
- Team member details
- Contact information

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

This project is proprietary to Gambix IT Services.

## Contact

For questions or support, contact:

- Email: info@gambixit.com
- Phone: +1 (555) 123-4567
