class Solution {
    public int getSum(int a, int b) {
        // repeat the steps until the carry value is 0
        while(b != 0) {
            int carrybits = (a & b) << 1;
            a = a ^ b; // add and store sum on a (this ignores carrybits)
            b = carrybits; // now b represents the carry value
        }
        return a;
    }
}