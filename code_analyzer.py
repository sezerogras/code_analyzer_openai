import timeit
import memory_profiler
import radon.complexity as radon_complexity
import ast

def measure_execution_time(code, setup="pass", repeat=5):
    """Kodun çalışma süresini ölçer."""
    timer = timeit.Timer(lambda: exec(code))
    return timer.repeat(repeat, 1)

def profile_memory_usage(func, *args, **kwargs):
    """Kodun bellek kullanımını ölçer."""
    mem_usage = memory_profiler.memory_usage((func, args, kwargs))
    return max(mem_usage) - min(mem_usage)

def analyze_complexity(code):
    """Kodun karmaşıklık seviyesini analiz eder."""
    tree = ast.parse(code)
    complexity_scores = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            complexity_scores.append(radon_complexity.cc_visit(node))
    return complexity_scores

def run_performance_analysis(code):
    """Kodun performans analizini yapar."""
    execution_times = measure_execution_time(code)
    
    def test_func():
        exec(code)

    memory_usage = profile_memory_usage(test_func)
    complexity_report = analyze_complexity(code)

    return {
        "execution_times": execution_times,
        "memory_usage": memory_usage,
        "complexity_report": complexity_report
    }
