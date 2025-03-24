import os
import re

# Define the mapping of file prefixes to new names
file_mapping = {
    # Topic 3.3: Random Sampling and Data Collection
    "SG_RandomSamplingandDataCollection": "3-3_Answers",
    "TB_RandomSamplingandDataCollection": "3-3_Questions",
    
    # Topic 3.5: Introduction to Experimental Design
    "SG_IntroductiontoExperimentalDesign": "3-5_Answers",
    "TB_IntroductiontoExperimentalDesign": "3-5_Questions",
    
    # Topic 3.6: Selecting an Experimental Design
    "SG_SelectinganExperimentalDesign": "3-6_Answers",
    "TB_SelectinganExperimentalDesign": "3-6_Questions",
    
    # Topic 5.7: Sampling Distributions for Sample Means
    "SG_SamplingDistributionsforSampleMeans": "5-7_Answers",
    "TB_SamplingDistributionsforSampleMeans": "5-7_Questions",
    
    # Topic 5.8: Sampling Distributions for Differences in Sample Means
    "SG_SamplingDistributionsforDifferencesinSampleMeans": "5-8_Answers",
    "TB_SamplingDistributionsforDifferencesinSampleMeans": "5-8_Questions",
    
    # Topic 7.6: Confidence Intervals for the Difference of Two Means
    "SG_ConfidenceIntervalsfortheDifferenceofTwoMeans": "7-6_Answers",
    "TB_ConfidenceIntervalsfortheDifferenceofTwoMeans": "7-6_Questions",
    
    # Topic 7.7: Justifying a Claim About the Difference of Two Means Based on a Confidence Interval
    "SG_JustifyingaClaimAbouttheDifferenceofTwoMeansBasedonaConfidenceInterval": "7-7_Answers",
    "TB_JustifyingaClaimAbouttheDifferenceofTwoMeansBasedonaConfidenceInterval": "7-7_Questions",
    
    # Topic 7.8: Setting Up a Test for the Difference of Two Population Means
    "SG_SettingUpaTestfortheDifferenceofTwoPopulationMeans": "7-8_Answers",
    "TB_SettingUpaTestfortheDifferenceofTwoPopulationMeans": "7-8_Questions",
    
    # Topic 7.9: Carrying Out a Test for the Difference of Two Population Means
    "SG_CarryingOutaTestfortheDifferenceofTwoPopulationMeans": "7-9_Answers",
    "TB_CarryingOutaTestfortheDifferenceofTwoPopulationMeans": "7-9_Questions"
}

def rename_pdfs():
    # Get all PDF files in the current directory
    pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    
    # Filter out files we don't want to rename (like the exam PDF)
    quiz_pdfs = [f for f in pdf_files if f.startswith(('SG_', 'TB_'))]
    
    renamed_count = 0
    skipped_count = 0
    failed_count = 0
    renamed_files = []
    
    print(f"Found {len(quiz_pdfs)} quiz PDF files to process")
    
    # Process each file
    for old_filename in quiz_pdfs:
        # Find the matching prefix
        matched = False
        for prefix, new_name in file_mapping.items():
            if old_filename.startswith(prefix):
                new_filename = f"{new_name}.pdf"
                try:
                    # Check if the file already exists
                    if os.path.exists(new_filename):
                        print(f"SKIPPED: {old_filename} → {new_filename} (target already exists)")
                        skipped_count += 1
                    else:
                        # Rename the file
                        os.rename(old_filename, new_filename)
                        print(f"RENAMED: {old_filename} → {new_filename}")
                        renamed_count += 1
                        renamed_files.append((old_filename, new_filename))
                    matched = True
                    break
                except Exception as e:
                    print(f"ERROR: Could not rename {old_filename}: {str(e)}")
                    failed_count += 1
                    matched = True
                    break
        
        if not matched:
            print(f"UNMATCHED: No matching pattern found for {old_filename}")
            skipped_count += 1
    
    # Print summary
    print("\nRename Summary:")
    print(f"  - Successfully renamed: {renamed_count} files")
    print(f"  - Skipped/Unmatched: {skipped_count} files")
    print(f"  - Failed: {failed_count} files")
    
    if renamed_count > 0:
        print("\nRenaming details:")
        for old, new in renamed_files:
            print(f"  {old} → {new}")

if __name__ == "__main__":
    print("Starting PDF renaming process...")
    rename_pdfs()
    print("\nPDF renaming process completed.") 