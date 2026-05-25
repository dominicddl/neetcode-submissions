class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create a hashmap with a mapping of the index value to index
        Map<Integer, Integer> indexMap = new HashMap<>();

        boolean isTwoSum; 
        int[] output = new int[2];

        // Store key-values in indexMap
        for (int i = 0; i < nums.length; i++) {
            // Calculate difference between target and value of current index 
            int diff = target - nums[i];
            if (indexMap.containsKey(diff)) {
                // Store into the output array the current index j and the key with
                // the value equal to diff
                output[0] = indexMap.get(diff);
                output[1] = i;
            }
            indexMap.put(nums[i], i);
        }

        return output;
    }
}
