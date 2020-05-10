INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_COMSYS comsys)

FIND_PATH(
    COMSYS_INCLUDE_DIRS
    NAMES comsys/api.h
    HINTS $ENV{COMSYS_DIR}/include
        ${PC_COMSYS_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    COMSYS_LIBRARIES
    NAMES gnuradio-comsys
    HINTS $ENV{COMSYS_DIR}/lib
        ${PC_COMSYS_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(COMSYS DEFAULT_MSG COMSYS_LIBRARIES COMSYS_INCLUDE_DIRS)
MARK_AS_ADVANCED(COMSYS_LIBRARIES COMSYS_INCLUDE_DIRS)

