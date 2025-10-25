# Example Inputs

This directory contains sample input files demonstrating different use cases and tones for the CarbonTrack Promoter AI agent.

## Available Examples

### 1. `sample_input.json` - Professional Tone
The default example showcasing a professional, business-oriented tone.

**Project**: CarbonTrack  
**Tone**: Professional  
**Use Case**: Sustainability app promotion

```bash
python src/main.py --input examples/sample_input.json
```

### 2. `sample_technical.json` - Technical Tone
A developer-focused example with technical language.

**Project**: DevTools Pro  
**Tone**: Technical  
**Use Case**: Developer tools promotion

```bash
python src/main.py --input examples/sample_technical.json
```

### 3. `sample_enthusiastic.json` - Enthusiastic Tone
An energetic, exciting example for consumer apps.

**Project**: FitQuest  
**Tone**: Enthusiastic  
**Use Case**: Fitness app promotion

```bash
python src/main.py --input examples/sample_enthusiastic.json
```

## Input File Format

All input files follow this JSON schema:

```json
{
  "project_name": "string",        // Required: Name of your project
  "website_url": "string",         // Required: URL to your project
  "description": "string",         // Required: Project description
  "key_features": ["string"],      // Required: Array of key features
  "tone": "string"                 // Optional: professional|casual|enthusiastic|technical
}
```

## Creating Your Own

1. Copy an existing example:
   ```bash
   cp examples/sample_input.json examples/my_project.json
   ```

2. Edit with your project details

3. Run the agent:
   ```bash
   python src/main.py --input examples/my_project.json
   ```

## Tone Guide

### Professional
- **Best for**: B2B products, enterprise software, serious applications
- **Style**: Formal, authoritative, results-focused
- **Example**: "Introducing a comprehensive solution for..."

### Casual
- **Best for**: Consumer apps, community projects, friendly brands
- **Style**: Conversational, approachable, relatable
- **Example**: "Hey everyone! Check out this cool new app..."

### Enthusiastic
- **Best for**: Product launches, exciting features, viral potential
- **Style**: Energetic, passionate, FOMO-inducing
- **Example**: "🎉 We're thrilled to announce..."

### Technical
- **Best for**: Developer tools, APIs, technical products
- **Style**: Detailed, architecture-focused, specs-oriented
- **Example**: "Built with a microservices architecture..."

## Tips

- **Keep features concise**: 3-6 bullet points work best
- **Clear value proposition**: Make the benefit obvious
- **Valid URLs**: Ensure website URLs are accessible
- **Appropriate tone**: Match tone to your audience
- **Test first**: Use `AUTO_POST=false` to preview before posting
