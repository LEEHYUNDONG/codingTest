class MyCircularDeque {
    private int[] arr;
    private int front;
    private int rear;
    private int size;

    public MyCircularDeque(int k) {
        arr = new int[k];
        size = k;
        front = -1;
        rear = -1;
    }
    
    public int prv(int v){
        return (v == 0) ? size - 1 : (v - 1)%size;
    }

    public int nxt(int v){
        return (v+1)%size;
    }

    public boolean insertFront(int value) {
        if (isFull())
            return false;
        if(front == -1){
            front = 0;
            rear = 0;
            arr[front] = value;
            return true;
        }
        front = prv(front);
        arr[front] = value;
        return true;
    }
    
    public boolean insertLast(int value) {
        if(isFull())
            return false;
        if(rear == - 1){
            front = 0;
            rear = 0;
            arr[rear] = value;
            return true;
        }
        rear = nxt(rear);
        arr[rear] = value;
        return true;
    }
    
    public boolean deleteFront() {
        if(isEmpty())
            return false;
        if(front == rear){
            front = -1;
            rear = -1;
            return true;
        }
        front = nxt(front);
        return true;
    }
    
    public boolean deleteLast() {
        if(isEmpty())
            return false;
        if(front == rear){
            front = -1;
            rear = -1;
            return true;
        }
        rear = prv(rear);
        return true;
    }
    
    public int getFront() {
        if(isEmpty())
            return -1;
        return arr[front];
    }
    
    public int getRear() {
        if(isEmpty())
            return -1;
        return arr[rear];
    }
    
    public boolean isEmpty() {
        return front == -1 && rear == -1;
    }
    
    public boolean isFull() {
        return front != -1 && front == nxt(rear);
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */