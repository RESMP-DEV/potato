# CME Tag Verification with Potato

This project implements a human-in-the-loop annotation interface for verifying AI-generated medical tags for Continuing Medical Education (CME) content.

## Overview

The CME tagging system uses Potato to create an efficient verification workflow where Subject Matter Experts (SMEs) can quickly verify or correct AI-generated tags including:
- Medical specialty classifications
- State/region assignments  
- Topic categorizations

## Project Structure

```
cme-tagging/
├── configs/
│   └── cme_config.yaml       # Main configuration file
├── data/
│   └── cme_samples.jsonl     # Sample CME documents with AI predictions
├── templates/
│   └── cme_layout.html       # Custom HTML template for CME display
├── scripts/
│   └── generate_sample_data.py  # Script to generate sample data
└── README.md                  # This file
```

## Quick Start

1. **Install Potato** (if not already installed):
```bash
pip install -r requirements.txt
```

2. **Run the annotation server**:

Option A: Using the provided script
```bash
cd project-hub/cme-tagging/scripts
./run_annotation.sh
```

Option B: Direct command from potato root
```bash
# From the potato root directory
python potato/flask_server.py start project-hub/cme-tagging/configs/cme_config.yaml -p 8000
```

3. **Access the interface**:
Open http://localhost:8000 in your browser

4. **Login**:
Any username is accepted (configured for open access)

## Configuration Details

### Data Format
The input data (`cme_samples.jsonl`) contains:
- `id`: Unique document identifier
- `text`: CME content text
- `predicted_tags`: JSON string with AI predictions
- `confidence`: Confidence score from AI model

### Annotation Schema
The interface presents two verification tasks:
1. **Specialty Verification**: Verify if the AI-predicted medical specialty is correct
2. **State Verification**: Verify if the geographic assignment is correct

Both include optional text fields for corrections when marked as incorrect.

### Keyboard Shortcuts
- Press `1`: Mark specialty as Correct
- Press `2`: Mark specialty as Incorrect  
- Press `3`: Mark specialty as Needs Edit
- Press `4`: Mark state as Correct
- Press `5`: Mark state as Incorrect
- Press `Enter`: Submit and move to next

## Customization

### Modify the Display Template
Edit `templates/cme_layout.html` to change how documents and tags are displayed.

### Add More Fields
Edit `configs/cme_config.yaml` to add additional annotation schemes for other tag types.

### Generate New Sample Data
Run the data generation script:
```bash
python scripts/generate_sample_data.py
```

## Integration with v0.1 Tagger

To use with real v0.1 tagger output:
1. Format tagger output as JSONL with required fields
2. Replace `data/cme_samples.jsonl` with your data
3. Update confidence thresholds in configuration if needed

## Output

Annotations are saved to `annotation_output/cme_tagging/` in JSON format, including:
- Verification decisions (correct/incorrect/needs_edit)
- Corrected values when applicable
- Annotation timestamps and duration

## Expected Workflow Efficiency

This interface is designed to be 12-30x faster than manual tagging:
- Keyboard shortcuts for rapid verification
- Clear display of AI predictions
- Streamlined correction interface
- Batch processing capabilities

## Contact

For questions or issues, please contact the RESMP-DEV team.