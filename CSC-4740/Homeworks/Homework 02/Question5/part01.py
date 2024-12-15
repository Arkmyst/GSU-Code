# Author: Asrar Syed
# Course Section: CSC 4740-002

# Data
FluidIQ = [122,103,148,137,0,101,102,72,148,116,107,131,110,84,125,110,113,95,66,103,142,84,116,110,116,97,84,142,84,97]
CrystallizedIQ = [77,77,91,107,0,87,89,63,91,99,101,90,75,82,99,95,100,93,80,91,96,91,84,81,82,74,72,106,85,81]
Vocabulary = [131,98,153,142,0,102,122,82,120,109,102,153,98,98,112,109,112,92,72,120,122,92,131,98,120,98,77,120,92,98]
InhibitoryControl = [81,69,89,106,0,75,86,57,97,95,101,93,71,93,98,91,99,97,84,96,92,102,90,86,91,67,76,104,97,91]
Memory = [86,97,109,105,0,94,97,67,105,105,105,101,97,82,105,101,105,94,86,97,109,82,70,101,101,86,74,109,86,97]
MentalFlexibility = [86,84,87,102,0,90,90,88,74,101,97,88,89,91,105,90,96,94,95,72,98,91,85,74,81,79,73,100,93,90]
ProcessingSpeed = [80,57,67,94,0,88,88,78,86,101,97,84,67,86,90,94,97,90,71,92,67,90,101,90,74,78,88,90,82,59]
AttentionProblem = [8.6,10,7.8,7.6,7.8,8.8,7.6,8.2,9.8,7.2,7.8,8.4,7.4,7.4,8.2,6.5,9.2,8.2,8,8,7,7.2,8.6,7.6,8,7.2,8,7.6,8,8.4]
AnxietyProblem = [7,8.5,8,6.6,6.8,7.7,7.6,8.5,9,7.3,7.6,8.8,8.8,8.2,9.7,7.7,7,8.5,8.3,7.9,8.3,7.6,7.6,7.6,7.3,9.4,7.9,5.3,5.6,6.6]
SocialProblems = [8,9,7.2,5.6,7.5,6.7,7,7,8.2,8.2,7,7,7.5,6.9,8,6.4,6.2,7.5,7,8.8,6.7,6.7,7.3,7.3,6.7,8.3,7,5.9,6.4,6.5]


# Remove the 4th index (fifth element) from each list
lists = [FluidIQ, CrystallizedIQ, Vocabulary, InhibitoryControl, Memory, MentalFlexibility, ProcessingSpeed, AttentionProblem, AnxietyProblem, SocialProblems]
for lst in lists:
    del lst[4]

# Output the updated lists
newFluidIQ = lists[0]
newCrystallizedIQ = lists[1]
newVocabulary = lists[2]
newInhibitoryControl = lists[3]
newMemory = lists[4]
newMentalFlexibility = lists[5]
newProcessingSpeed = lists[6]
newAttentionProblem = lists[7]
newAnxietyProblem = lists[8]
newSocialProblems = lists[9]


def find_outliers(data):
    if len(data) < 4:
        return "Data must have at least 4 points to find outliers."

    # Sort the data
    sorted_data = sorted(data)
    
    # Calculate Q1 and Q3
    n = len(sorted_data)
    Q1_index = n // 4
    Q3_index = 3 * n // 4
    Q1 = sorted_data[Q1_index]
    Q3 = sorted_data[Q3_index]
    
    # Calculate the Interquartile Range (IQR)
    IQR = Q3 - Q1
    
    # Determine the bounds for outliers
    lower_bound = Q1 - 3 * IQR
    upper_bound = Q3 + 3 * IQR
    print(lower_bound)
    print(upper_bound)

    # Identify outliers
    outliers = [x for x in data if x < lower_bound or x > upper_bound]
    
    return outliers

# Example usage
data = newInhibitoryControl
outliers = find_outliers(data)
print("Outliers:", outliers)
