import java.io.*;
class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		int T = Integer.parseInt(input);
		int ans = 0;
		int a,b;
		String[] sentence;
		
		for (int i = 0; i< T;i++){
			//[a,operend,b]
			input = br.readLine();
			sentence =input.split(" ");
			a= Integer.parseInt(sentence[0]);
			String operend = sentence[1];
			b = Integer.parseInt(sentence[2]);
			switch(operend){
				case "+":
					ans += a+b;
					break;
				case "-":
					ans += a-b;
					break;
				case "/":
					ans += a/b;
					break;
				case "*":
					ans += a*b;
					break;
				default:
					break;
			}
		}
		System.out.println(ans);
	}
}