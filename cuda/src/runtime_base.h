//
// Created by haoxin on 2019/8/1.
//

#ifndef STARXIN_RUNTIME_BASE_H
#define STARXIN_RUNTIME_BASE_H

#include "c_runtime_api.h"
#include <stdexcept>

#define API_BEGIN() try {

#define API_END()                                                              \
  }                                                                            \
  catch (std::runtime_error & _except_) {                                      \
    return DLSYSAPIHandleException(_except_);                                  \
  }                                                                            \
  return 0;


#define API_END_HANDLE_ERROR(Finalize)                                         \
  }                                                                            \
  catch (std::runtime_error & _except_) {                                      \
    Finalize;                                                                  \
    return DLSYSAPIHandleException(_except_);                                  \
  }                                                                            \
  return 0;


inline int DLSYSAPIHandleException(const std::runtime_error &e) {
    // TODO
    return -1;
}

#endif //STARXIN_RUNTIME_BASE_H
