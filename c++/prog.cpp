#include <iostream>
#include <limits>
#include <cmath>

template<typename T>
T next_above(const T& v){
    return std::nextafter(v,std::numeric_limits<T>::infinity()) ;
}
template<typename T>
T next_below(const T& v){
    return std::nextafter(v,-std::numeric_limits<T>::infinity()) ;
}

int main(){
  std::cout << "eps   : "<<std::numeric_limits<double>::epsilon()<< std::endl; // gives eps

  std::cout << "after : "<<next_above(1.0) - 1.0<< std::endl; // gives eps (the definition of eps)
  std::cout << "below : "<<next_below(1.0) - 1.0<< std::endl; // gives -eps/2

  // Note: this is what next_above does:
  std::cout << std::nextafter(std::numeric_limits<double>::infinity(),
     std::numeric_limits<double>::infinity()) << std::endl; // gives inf

  // while this is probably not what you need:
  std::cout << std::nextafter(std::numeric_limits<double>::infinity(),
     std::numeric_limits<double>::max()) << std::endl; // gives 1.79769e+308

}
