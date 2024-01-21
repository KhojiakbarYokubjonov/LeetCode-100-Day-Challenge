class Solution {
    public int climbStairs(int n) {
        if(n == 1 || n == 2) {return n;}
        List<Integer>steps = new ArrayList<>();
        steps.add(1);
        steps.add(2);
        for(int i=3; i<=n; i++) {
            int prev = steps.get(steps.size()-1);
            int prevprev = steps.get(steps.size()-2);
            steps.add(prev + prevprev);
        }
        
        
        return steps.get(steps.size()-1);
    }
}