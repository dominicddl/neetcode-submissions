class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        // First pass to calculate prefix 
        // Initialise first element to be 1 for the product of the first
        // element with itself
        res[0] = 1;
        // Calculate prefix
        for (int i = 1; i <= nums.length - 1; i++) {
            res[i] = nums[i - 1] * res[i - 1];
        }
        // Second pass to calculate postfix and multiply with each prefix
        int postfix = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            res[i] *= postfix;
            postfix *= nums[i];
        }
        return res;
    }
}  
