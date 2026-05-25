class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Boolean> numsMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            // Check if integer is in the HashMap 
            if (numsMap.containsKey(nums[i])) {
                return numsMap.get(nums[i]);
            }
            // If not in HashMap, add it to the HashMap and mark it as "Seen"
            numsMap.put(nums[i], true);
        }
        return false;
    }
}