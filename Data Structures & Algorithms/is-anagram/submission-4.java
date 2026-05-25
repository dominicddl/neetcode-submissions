class Solution {
    public boolean isAnagram(String s, String t) {
        // Base case if string length of s and t are not equal
        if (s.length() != t.length()) {
            return false;
        }

        // Initialise HashMaps to store characters of string s and string t 
        Map<Character, Integer> sFrequency = new HashMap<>();
        Map<Character, Integer> tFrequency = new HashMap<>();

        // Loop through String s and t to store frequency count of each character
        for (int i = 0; i < s.length(); i++) {
            sFrequency.put(s.charAt(i), sFrequency.getOrDefault(s.charAt(i), 0) + 1);
            tFrequency.put(t.charAt(i), tFrequency.getOrDefault(t.charAt(i), 0) + 1);
        }

        return sFrequency.equals(tFrequency);
     }
}
