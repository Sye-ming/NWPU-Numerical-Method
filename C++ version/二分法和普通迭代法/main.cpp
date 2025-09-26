#include <iostream>
#include <cmath>
#include <windows.h>


double f_origial(double x){
    return 2 * std::exp(-x) - std::sin(x);
}

double f_iterative(double x){
    return - std::log(std::sin(x) / 2.0);
}

double Bisection_method(double a , double b , double epsilon){
    double x_avg = 0;
    double x_1 = 0;
    double x_2 = 0;

    constexpr double eps = 1e-12;       // 宏定义没有作用域，容易污染全局变量,不利于调试

    x_avg = (a + b) / 2;

    do {
        if(fabs(f_origial(x_avg)) <= eps){
            return x_avg;
        }
        else if(f_origial(x_avg) * f_origial(a) < 0 and f_origial(x_avg) * f_origial(b) > 0){

            b = x_avg;

        }
        else if(f_origial(x_avg) * f_origial(b) < 0 and f_origial(x_avg) * f_origial(a) > 0){
            a = x_avg;

        }
        x_1 = x_avg;
        x_avg = (a + b)/2;
    } while (std::fabs(x_1 - x_2) >= epsilon);

    return x_avg;

}



double Simple_Iteration_Method(double epsilon , double x_0){
    double x_b = 0;
    do{
        x_b = x_0;
        x_0 = f_iterative(x_0);

    }while(std::fabs(x_b - x_0) >= epsilon);

    return x_0;
}


double Aikten_Acceleration_Formula(double x_0 , double x_1 , double x_2 ){
    return x_0 - std::pow(x_1 - x_0 , 2) / (x_2 - 2 * x_1 + x_0);
}


double Aitken_Method(double x_0, double epsilon){

    double x_1 = 0;
    double x_2 = 0;

    double x_2_old = 0;

    x_1 = f_iterative(x_0);
    x_2 = f_iterative(x_1);

    while(std::fabs(x_1 - x_0) >= epsilon){
        x_2_old = x_2;
        x_2 = Aikten_Acceleration_Formula(x_0 , x_1 , x_2);
        x_0 = x_1;
        x_1 = x_2_old;
    }

    return x_1;
}


double Steffensen_Acceleration_Formula(double x_0){
    return x_0 - (std::pow(f_iterative(x_0) - x_0 , 2)) / (f_iterative(f_iterative(x_0)) - 2 * f_iterative(x_0) + x_0);
}

double Steffensen_Method(double x_0 , double epsilon){
    double x_1 = 0;

    while (std::fabs(x_1 - x_0) >= epsilon){
        x_1 = Steffensen_Acceleration_Formula(x_0);
        x_0 = x_1;
    }

    return x_1;
}




int main() {

    SetConsoleOutputCP(65001);   // 输出编码
    SetConsoleCP(65001);         // 输入编码

/*           二分法、简单迭代法及其加速法求解非线性方程             */

    double a = 0;
    double b = 0;
    double epsilon = 0;
    double x_0 = 0;

    std::cout << "请输入隔根区间：" << std::endl;
    std::cin >> a >> b;
    if(a >= b or f_origial(a) * f_origial(b) >= 0){
        std::cerr << "错误！请检查输入的区间是否符合要求。";
        return 1;
    }

    std::cout << "请输入绝对误差限：" << std::endl;
    std::cin >> epsilon;

    std::cout << "请输入初值x_0：" << std::endl;
    std:: cin >> x_0;

    std::cout << "二分法求解结果" << Bisection_method(a , b , epsilon) << std::endl;
    std::cout << "简单迭代法求解结果：" << Simple_Iteration_Method(epsilon , x_0) << std::endl;
    std::cout << "Aitken加速法求解结果：" << Aitken_Method(x_0 , epsilon) << std::endl;
    std::cout << "Steffensen加速法求解结果：" << Steffensen_Method(x_0 , epsilon) << std::endl;

    return 0;
}

