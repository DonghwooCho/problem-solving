import java.util.*;

class Main {
    public static void main(String[] args) {

    // 1. 입력 받기
    Scanner scanner = new Scanner(System.in);

    int N = Integer.parseInt(scanner.nextLine());
    int[] length = new int[N-1];
    int[] price = new int[N];

    for(int i = 0; i < N - 1; i++) {
        length[i] = Integer.parseInt(scanner.next());
    }
    for(int i = 0; i < N; i++) {
        price[i] = Integer.parseInt(scanner.next());
    }

    // 2. 최소 비용 출력 하기
    int cost = 0;
    int min_price = price[0];
    for(int i = 0; i < N - 1; i++) {
        if(min_price > price[i]) {
            min_price = price[i];
        }
        cost += min_price * length[i];
    }
    
    scanner.close();
    System.out.println(cost);
    }
}