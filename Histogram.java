import java.util.Scanner;

public class Histogram {
    int lowerBound;
    int upperBound;
    int[] myArray;

    public Histogram(int lowerBound, int upperBound){
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
        myArray = new int[upperBound + 1];
        for(int i = 0; i < myArray.length; i++){
            myArray[i] = 0;
        }
    }

    public boolean add(int i){
        if(i >= lowerBound && i<=upperBound){
            myArray[i] += 1;// i is num
            return true;
        }
        return false;
    }
    public String toString(){
        String s = "";
        for(int a =lowerBound;a<=upperBound;a++){
            s += a +":";
            for(int b = 0; b< myArray[a];b++){
                s += "*";
            }s+="\n";
        }return s;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Range to get started: ");
        int lowerBound = sc.nextInt();
        int upperBound = sc.nextInt();
        Histogram histogram = new Histogram(lowerBound,upperBound);
        System.out.print(">Enter Command: ");
        while(sc.hasNextLine()){
            String input  = sc.nextLine();
            if(input.equals("add")){
                System.out.print("Enter number: ");
                String num  = sc.nextLine();
                for(String a : num.split(" ")) {
                    if (histogram.add(Integer.parseInt(a)) == false) {
                        System.out.print(a + " " + "is not in the range" + "\n");
                    }
                }
            }else if(input.equals("print")){
                System.out.println(histogram);
            }else if(input.equals("quit")) {
                System.out.println("bye");
                break;
            }
            System.out.print(">");
        }
    }
}

