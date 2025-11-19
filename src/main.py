import argparse
import sys
import os

# Add the current directory to sys.path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_collector import DataCollector
from data_structurer import DataStructurer
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="Research Agent - Corporate Intelligence")
    parser.add_argument("--company", type=str, required=True, help="Company Name or Website to research")
    args = parser.parse_args()

    company_identifier = args.company
    print(f"Starting research for: {company_identifier}")

    # Phase 1: Data Collection
    collector = DataCollector()
    raw_data = collector.collect_data(company_identifier)

    # Phase 2: Data Structuring
    structurer = DataStructurer()
    structured_data = structurer.structure_data(raw_data)

    # Phase 3: Report Synthesis
    generator = ReportGenerator()
    report_content = generator.generate_report(structured_data)

    # Save Report
    filename = f"{company_identifier.replace(' ', '_')}_Research_Report.md"
    generator.save_report(report_content, filename)
    print(f"Research complete! Report saved to {filename}")

if __name__ == "__main__":
    main()
