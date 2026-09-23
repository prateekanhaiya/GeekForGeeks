import java.util.Scanner;

class GFG {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        
        for (int i = 0; i < n; i++){
            
            int star = 2*n -1 - (2*i);
            
            System.out.println(" ".repeat(i) + "*".repeat(star));
            
        }
        
    }
}