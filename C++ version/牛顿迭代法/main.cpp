#include <iostream>
#include <cmath>
#include <windows.h>


//      原始函数
double function_original(double x){
    return std::pow(x , 3) - std::pow(x , 2) - 1;
}


//      求导函数
double derivative(double x){
    constexpr double delta_x = 1e-8;
    return (function_original(x + delta_x) - function_original(x))/(delta_x);
}


//      迭代函数
double function_iteriate(double x){
    return x - function_original(x) / derivative(x);
}

// 检查一阶导函数是否符合条件
examine_derivative(double a , double b){
    constexpr double eps = 1e-8;

    for (double x = a; x < b; x += 0.01){
        if (derivative(x) < eps){
            return false;
        }
    }
    return true;
}


int main(){

    // #ifdef _WIN32
    //     system("chcp 65001 >nul");
    // #endif

    // SetConsoleOutputCP(65001);   // 输出编码
    // SetConsoleCP(65001);         // 输入编码

    double x_intial = 0;
    double x_curr = 0;
    double epsilon = 0;
    double a = 0;
    double b = 0;

    constexpr double eps = 1e-10;

    std::cout << "请输入区间[a,b]：" << std::endl;
    std::cin >> a >> b;

    // 检查是否符合Newton迭代法的条件
    if (function_original(a) * function_original(b) > 0) {
        std::cerr << "区间[a,b]不符合Newton迭代法的条件" << std::endl;
    }
    else if (examine_derivative(a, b) == false) {
        std::cerr << "一阶导数不符合条件" << std::endl;
    }

    std::cout << "请输入初值：" << std::endl;
    std::cin >> x_intial;

    std::cout << "请输入绝对误差限：" << std::endl;
    std::cin >> epsilon;

    x_curr = function_iteriate(x_intial);
    for (int i = 0; std::fabs(x_curr - x_intial) > epsilon; i++) {
        x_intial = x_curr;
        x_curr = function_iteriate(x_intial);
    }
    std::cout << "Newton迭代法结果为：" << x_curr << std::endl;




    return 0;
}
