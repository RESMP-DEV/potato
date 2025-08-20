#!/usr/bin/env python3
"""
Minimal CME tagging prototype generator for Potato annotation
"""

import json
import random
from pathlib import Path

def generate_sample_cme_documents():
    """Generate sample CME documents that mimic v0.1 tagger output"""
    
    samples = [
        {
            "doc_id": "cme_001",
            "text": "Recent advances in CAR-T cell therapy have shown promising results in treating B-cell lymphomas. The FDA-approved tisagenlecleucel has demonstrated overall response rates of 52% in adult patients with relapsed or refractory large B-cell lymphoma.",
            "predicted_tags": {
                "specialty": "Oncology",
                "state": "National",
                "topics": ["Treatment", "Research", "FDA Approval"]
            },
            "confidence": 0.92
        },
        {
            "doc_id": "cme_002", 
            "text": "New California guidelines for hypertension management in elderly patients recommend starting with lower doses of ACE inhibitors or ARBs, with careful monitoring of renal function and potassium levels.",
            "predicted_tags": {
                "specialty": "Geriatrics",
                "state": "CA",
                "topics": ["Guidelines", "Treatment", "Medication Management"]
            },
            "confidence": 0.78
        },
        {
            "doc_id": "cme_003",
            "text": "Pediatric vaccination schedules have been updated to include the new RSV vaccine for infants. The CDC recommends administration at 2, 4, and 6 months of age for optimal protection.",
            "predicted_tags": {
                "specialty": "Pediatrics",
                "state": "National", 
                "topics": ["Prevention", "Vaccination", "CDC Guidelines"]
            },
            "confidence": 0.95
        },
        {
            "doc_id": "cme_004",
            "text": "Emergency department protocols in Texas for stroke management emphasize the importance of the golden hour. Door-to-needle time for tPA administration should be under 60 minutes.",
            "predicted_tags": {
                "specialty": "Emergency Medicine",
                "state": "TX",
                "topics": ["Treatment", "Protocols", "Time-Sensitive Care"]
            },
            "confidence": 0.88
        },
        {
            "doc_id": "cme_005",
            "text": "Machine learning models for radiology image analysis are showing promise in early detection of lung nodules. A recent study in New York hospitals showed 23% improvement in detection rates.",
            "predicted_tags": {
                "specialty": "Radiology",
                "state": "NY",
                "topics": ["AI/ML", "Diagnosis", "Research"]
            },
            "confidence": 0.73
        },
        {
            "doc_id": "cme_006",
            "text": "Updates to diabetes management include continuous glucose monitoring integration with insulin pumps. Endocrinologists in Florida report improved HbA1c levels in 78% of patients.",
            "predicted_tags": {
                "specialty": "Endocrinology",
                "state": "FL",
                "topics": ["Technology", "Treatment", "Diabetes Management"]
            },
            "confidence": 0.85
        },
        {
            "doc_id": "cme_007",
            "text": "Neurology grand rounds discussed the latest in migraine prevention with CGRP antagonists showing 50% reduction in monthly migraine days for chronic sufferers.",
            "predicted_tags": {
                "specialty": "Neurology",
                "state": "Unknown",
                "topics": ["Treatment", "Prevention", "Pharmacology"]
            },
            "confidence": 0.81
        },
        {
            "doc_id": "cme_008",
            "text": "Surgical techniques for minimally invasive cardiac procedures have evolved. Pennsylvania cardiac centers report reduced recovery times from 6 weeks to 2 weeks.",
            "predicted_tags": {
                "specialty": "Cardiac Surgery",
                "state": "PA",
                "topics": ["Surgery", "Innovation", "Recovery"]
            },
            "confidence": 0.90
        },
        {
            "doc_id": "cme_009",
            "text": "Psychiatry updates include new evidence for ketamine-assisted therapy in treatment-resistant depression. Clinical trials show 70% response rate within 24 hours.",
            "predicted_tags": {
                "specialty": "Psychiatry",
                "state": "National",
                "topics": ["Treatment", "Mental Health", "Clinical Trials"]
            },
            "confidence": 0.76
        },
        {
            "doc_id": "cme_010",
            "text": "Dermatology advances in psoriasis treatment with JAK inhibitors show complete skin clearance in 40% of patients after 16 weeks of treatment.",
            "predicted_tags": {
                "specialty": "Dermatology",
                "state": "Unknown",
                "topics": ["Treatment", "Immunology", "Skin Conditions"]
            },
            "confidence": 0.83
        }
    ]
    
    # Add some intentionally incorrect tags for testing
    incorrect_samples = [
        {
            "doc_id": "cme_011",
            "text": "Orthopedic surgeons recommend early mobilization after knee replacement surgery to prevent DVT and improve outcomes.",
            "predicted_tags": {
                "specialty": "Cardiology",  # Wrong!
                "state": "CA",
                "topics": ["Surgery", "Prevention"]
            },
            "confidence": 0.45
        },
        {
            "doc_id": "cme_012",
            "text": "Ophthalmology update: New treatments for macular degeneration using anti-VEGF injections show promising results.",
            "predicted_tags": {
                "specialty": "Optometry",  # Close but wrong!
                "state": "TX",
                "topics": ["Treatment", "Vision"]
            },
            "confidence": 0.58
        }
    ]
    
    return samples + incorrect_samples

def create_potato_config():
    """Create a Potato configuration file for CME tagging"""
    
    config = {
        "data_files": ["potato_data/cme_samples.jsonl"],
        "out_name": "cme_annotations",
        "output_annotation_dir": "potato_output/",
        "output_annotation_format": "json",
        "annotation_schemes": [
            {
                "annotation_type": "radio",
                "name": "verification",
                "description": "Is the AI-generated specialty tag correct?",
                "labels": [
                    {"name": "correct", "key_value": "1"},
                    {"name": "incorrect", "key_value": "2"},
                    {"name": "needs_edit", "key_value": "3"}
                ]
            },
            {
                "annotation_type": "text",
                "name": "corrected_specialty",
                "description": "If incorrect, what should the specialty be?",
                "optional": True
            },
            {
                "annotation_type": "radio", 
                "name": "state_verification",
                "description": "Is the state tag correct?",
                "labels": [
                    {"name": "correct", "key_value": "4"},
                    {"name": "incorrect", "key_value": "5"}
                ]
            },
            {
                "annotation_type": "text",
                "name": "corrected_state",
                "description": "If incorrect, what should the state be?",
                "optional": True
            }
        ],
        "html_layout": True,
        "display_columns": ["text", "predicted_tags"],
        "users_per_instance": 1,
        "edits_allowed": True
    }
    
    return config

def setup_potato_project():
    """Set up the complete Potato project structure"""
    
    # Create directories
    base_dir = Path("potato-cme")
    base_dir.mkdir(exist_ok=True)
    (base_dir / "potato_data").mkdir(exist_ok=True)
    (base_dir / "potato_output").mkdir(exist_ok=True)
    
    # Generate sample documents
    samples = generate_sample_cme_documents()
    
    # Write samples to JSONL file
    samples_file = base_dir / "potato_data" / "cme_samples.jsonl"
    with open(samples_file, 'w') as f:
        for sample in samples:
            # Format for Potato display
            potato_item = {
                "id": sample["doc_id"],
                "text": sample["text"],
                "predicted_tags": json.dumps(sample["predicted_tags"]),
                "confidence": sample["confidence"]
            }
            f.write(json.dumps(potato_item) + '\n')
    
    print(f"✅ Created {len(samples)} sample CME documents")
    
    # Create Potato config
    config = create_potato_config()
    config_file = base_dir / "cme_config.yaml"
    
    # Write YAML config
    import yaml
    with open(config_file, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)
    
    print(f"✅ Created Potato configuration at {config_file}")
    
    # Create a simple run script
    run_script = base_dir / "run_annotation.sh"
    with open(run_script, 'w') as f:
        f.write("""#!/bin/bash
# Run Potato annotation server for CME tagging

echo "Starting Potato annotation server..."
echo "Access at: http://localhost:8000"
echo "Press Ctrl+C to stop"

cd ..
python potato/potato/flask_server.py start potato-cme/cme_config.yaml -p 8000
""")
    
    run_script.chmod(0o755)
    print(f"✅ Created run script at {run_script}")
    
    print("\n" + "="*50)
    print("🎉 Potato CME Tagging Setup Complete!")
    print("="*50)
    print(f"\n📁 Project location: {base_dir.absolute()}")
    print(f"📊 Sample documents: {len(samples)}")
    print("\n🚀 To start annotation:")
    print("   cd potato-cme")
    print("   ./run_annotation.sh")
    print("\nOr run directly:")
    print("   python potato/potato/flask_server.py start potato-cme/cme_config.yaml -p 8000")

if __name__ == "__main__":
    setup_potato_project()