class A{
	private int a = 1;
	public int geta(){
		return a;
	}
}

class B extends A{
	int b = 10;
	int c = 20;
	public int get(){
		return b;
	}
}

class RetOb{
	public static void main(String[] args) {
		A ob = new B();
		System.out.println(ob.geta());
	}
}
