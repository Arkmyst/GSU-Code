/*
  Author: Asrar Syed
  Program: A program that finds the “smallest” and “largest” words in a series of words.
*/

#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 21  // 20 characters + null terminator

int main() {
    char current_word[MAX_LENGTH];
    char smallest_word[MAX_LENGTH];
    char largest_word[MAX_LENGTH];
    int first_word = 1;

    // Initialize with empty strings
    smallest_word[0] = '\0';
    largest_word[0] = '\0';

    while (1) {
        printf("Enter word: ");
        scanf("%20s", current_word);

        // Check if word is four letters long
        if (strlen(current_word) == 4) {
            break;
        }

        // If it is the first word, set it as both smallest and largest
        if (first_word) {
            strcpy(smallest_word, current_word);
            strcpy(largest_word, current_word);
            first_word = 0;
            continue;
        }

        // Compare with smallest word
        if (strcmp(current_word, smallest_word) < 0) {
            strcpy(smallest_word, current_word);
        }

        // Compare with largest word
        if (strcmp(current_word, largest_word) > 0) {
            strcpy(largest_word, current_word);
        }
    }

    // Print results
    printf("Smallest word: %s\n", smallest_word);
    printf("Largest word: %s\n", largest_word);

    return 0;
}