func countVowels(word string) int64 {
    vowel := int64(0)
    ifCase := int64(0)
    for i, v := range word{
        switch v{
            case 'a', 'e', 'i', 'o', 'u':
                ifCase += int64(i) +1
        }
        vowel += ifCase 
    }
    return vowel
}