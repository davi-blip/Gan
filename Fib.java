public class Fib {
    int n;

    public static int fibonacciRecursive(int n) {
        if (n == 0) {
            return 0;
        }if (n == 1) {
            return 1;
        } else {
            return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
        }
    }

    public static int recursiveMaxDigit(int num) {
        if (num / 10 == 0) {
            return num;
        } else {
            int b = num % 10;//2
            int max = recursiveMaxDigit(num / 10);
            if (b > max) {
                return b;
            } else {
                return max;
            }
        }
    }
    public static int iterativeMaxDigit(int num){
        int a = 0;
        while (num != 0){
            int b = num % 10;
            if(a<b){
                a = b;
            }
            num = num /10;
        }return a;
    }
    public static void main(String[] args) {
        int num  = 13442;
        System.out.println(recursiveMaxDigit(num));
        System.out.println(iterativeMaxDigit(num));
        int n = 10;
        System.out.println(fibonacciRecursive(n));
    }
}