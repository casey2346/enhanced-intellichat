"""
Utils Package for Enhanced AI Assistant
Contains smart sorting and enhanced understanding functionality
"""

from .smart_sort import smart_sort, generate_sort_example, benchmark_sorting_algorithms
from .enhanced_understanding import EnhancedUnderstandingSystem, enhance_response_understanding

__all__ = [
    'smart_sort',
    'generate_sort_example',
    'benchmark_sorting_algorithms',
    'EnhancedUnderstandingSystem',
    'enhance_response_understanding'
]

__version__ = '1.0.0'
__author__ = 'Enhanced AI Assistant Team'
__description__ = 'Advanced utility modules for intelligent conversation and data processing'