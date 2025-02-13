
__all__ = ['API_VERSION', 'ARCHITECTURES', 'COSTS', 'DRIVERS',
           'DEFAULT_FILE_CHUNK_SIZE', 'DEBIAN_FLAVORS', 'RHEL_FLAVORS',
           'SUPPORTED_ARCHITECTURES', 'SUPPORTED_DISTRIBUTIONS',
           'DEFAULT_REQUEST_TIMEOUT']


# YYYYMMDD format for API version
API_VERSION = '20210512'
COSTS = [str(i) for i in range(5)]
ARCHITECTURES = ('x86_64', 'aarch64', 'ppc64le')
DRIVERS = ('docker', 'opennebula')
SUPPORTED_ARCHITECTURES = ['x86_64', 'i686', 'amd64', 'arm64', 'aarch64',
                           'ppc64le']
SUPPORTED_DISTRIBUTIONS = ['almalinux', 'centos', 'ubuntu', 'debian']
RHEL_FLAVORS = ('rhel', 'fedora', 'centos', 'almalinux', 'cloudlinux')
DEBIAN_FLAVORS = ('debian', 'ubuntu', 'raspbian')


DEFAULT_FILE_CHUNK_SIZE = 8388608  # 8 megabytes in bytes
DEFAULT_REQUEST_TIMEOUT = 60  # 1 minute