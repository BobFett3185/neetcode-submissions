class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())  // first check to avoid creating map unneccesarily 
            return false;

        unordered_map<char, int> countS; // map for first string
        unordered_map<char, int> countT;  // map for second string
        for (int i = 0; i < s.length(); i++) { // add each string element to the map
            countS[s[i]]++;     // map[element] ++ to increment counts of the element
            countT[t[i]]++;
        }
        return countS == countT;
        
        
    }
};
