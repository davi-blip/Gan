//Written by Jianyuan Gan

public class Random {
    private int p1;
    private int p2;
    private int m;
    private int s;

    /**
     * @param p1 constant prime number
     * @param p2 constant prime number
     * @param m  constant prime number
     */
    public Random(int p1, int p2, int m){
        this.p1 = p1;
        this.p2 = p2;
        this.m = m;

        s = 0;//initialize seed number
    }

    /**
     * @param seed initial value of S
     */
    public void setSeed(int seed){
         this.s = seed;
    }

    /**
     * @return the maximum value of m
     */
    public int getMaximum(){
        return m;
    }

    /**
     * @return Method to return a random number
     */
    public int random(){
        s = (p1*s+p2)%m;
        return s;
    }

    /**
     * @param lower
     * @param upper
     * @return method to return a random integer value between lower to upper
     */
    public int randomInteger(int lower, int upper){
        if((upper-lower)<0){
            int tmp = lower;
            lower = upper;
            upper = tmp;
        }
        int randomNumber = (random() % (upper + 1 - lower))+lower;
        return randomNumber;
    }

    /**
     * @return return a boolean value randomly.
     */
    public boolean randomBoolean(){
        return random() % 2 == 0;
    }

    /**
     * @param lower
     * @param upper
     * @return a double random value between lower to upper.
     */
    public double randomDouble(double lower,double upper){
        if((upper -lower)<0) {
            double tmp = lower; //
            lower = upper;
            upper = tmp;
        }
        double randomDouble = (double) random();
        while (randomDouble > (upper + 1 - lower)) {
            //keep iterating until it less than the range. in case of it out of lower, plus lower so that
            //it wont be out of range.
            randomDouble /= (upper+1  - lower);
        }
        return randomDouble + lower;
    }

    public static void main(String[] args) {
        //cases to test my code
        Random num = new Random(7919,65537,102611);
        System.out.println(num.getMaximum());
        System.out.println(num.random());
        System.out.println(num.randomInteger(1,5));
        System.out.println(num.randomBoolean());
        System.out.println(num.randomDouble(1.0,5.0));
        System.out.println();
        System.out.println(num.getMaximum());
        System.out.println(num.random());
        System.out.println(num.randomInteger(1,5));
        System.out.println(num.randomBoolean());
        System.out.println(num.randomDouble(1.0,5.0));
        System.out.println();
        System.out.println(num.getMaximum());
        System.out.println(num.random());
        System.out.println(num.randomInteger(1,5));
        System.out.println(num.randomBoolean());
        System.out.println(num.randomDouble(1.0,5.0));
        System.out.println();
        System.out.println(num.getMaximum());
        System.out.println(num.random());
        System.out.println(num.randomInteger(1,5));
        System.out.println(num.randomBoolean());
        System.out.println(num.randomDouble(1.0,5.0));
        System.out.println();
        System.out.println(num.getMaximum());
        System.out.println(num.random());
        System.out.println(num.randomInteger(1,5));
        System.out.println(num.randomBoolean());
        System.out.println(num.randomDouble(1.0,5.0));
    }
}
