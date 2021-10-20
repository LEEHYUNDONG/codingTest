#include <iostream>
#include <deque>
using namespace std;
void showAll(deque<int> dq)
{
    while (!dq.empty())
    {
        cout << dq.front() << ' ';
        dq.pop_front();
    }
}

int main(void)
{
    deque<int> dq;
    dq.push_back(10);
    dq.push_back(20);
    dq.push_front(30);

    cout << "Show all queue elements : ";
    showAll(dq);

    cout << "\nq.size() : " << dq.size();
    cout << "\nq.front() : " << dq.front();
    cout << "\nq.back() : " << dq.back();

    cout << "\nq.pop_front()\n";
    dq.pop_front();
    cout << "Show all queue elements : ";
    showAll(dq);

    cout << "\ndq.pop_back()\n";
    dq.pop_back();
    cout << "Show all queue elements : ";
    showAll(dq);

    dq.clear();
    cout << "\nShow all queue elements" << endl;
    showAll(dq);

    return 0;
}