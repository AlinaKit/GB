<style>
fst { font-size:16px; font-weight: 900; box-shadow: 0 0 10px 3px rgba(255, 152, 152, 0.2); background-color: rgba(255, 152, 152, 0.14); }
snd { font-size:15px; font-weight: 800; box-shadow: 0 0 10px 3px rgba(255, 255, 152, 0.2); background-color: rgba(255, 255, 152, 0.14); }
trd { font-size:14px; font-weight: 700; box-shadow: 0 0 10px 3px rgba(152, 255, 152, 0.2); background-color: rgba(152, 255, 152, 0.14); }
fth { font-size:13px; font-weight: 600; box-shadow: 0 0 10px 3px rgba(152, 152, 255, 0.2); background-color: rgba(152, 152, 255, 0.14); }
ffth { font-size:12px; font-weight: 500; box-shadow: 0 0 10px 3px rgba(255, 152, 255, 0.2); background-color: rgba(255, 152, 255, 0.14); }
</style>

# Подсказки по ошибкам

## Структура

|                                      |                                                                                                 |
|:-------------------------------------|:------------------------------------------------------------------------------------------------|
| <fst>BaseException                   | "Стартовый" класс исключений, от которого наследуются остальные исключения ниже по иерархии     |
| * <snd>BaseExceptionGroup            | Не перехватывается программистом, нужен для создания групповых исключений                       |
| * <snd>GeneratorExit                 | Не перехватывается программистом, генератор сообщает о завершении работы                        |
| * <snd>KeyboardInterrupt             | Не перехватывается программистом, пользователь нажал сочетание клавиш для завершения программы  |
| * <snd>SystemExit                    | Не перехватывается программистом, программа сообщает о завершении                               |
| * <snd>Exception                     | Перехват ошибки, используется как базовое для наследования собственными классами-исключениями   |
| * * <trd>ArithmeticError             | Арифмитическая ошибка                                                                           |
| * * * <fth>FloatingPointError        |                                                                                                 |
| * * * <fth>OverflowError             |                                                                                                 |
| * * * <fth>ZeroDivisionError         |                                                                                                 |
| * * <trd>AssertionERROR              | Ошибка при вызове резерва-asset                                                                 |
| * * <trd>AttributeError              | Проблема с доступом к атрибуту                                                                  |
| * * <trd>BufferError                 | Проблема с буффером обмена                                                                      |
| * * <trd>EOFError                    | Проблема с концом файла                                                                         |
| * * <trd>ExceptionGroup              | Группа исключений для создания родительского исключения для групповых исключений и их обработки |
| * * <trd>ImportError                 | Проблемы с импортом                                                                             |
| * * * <fth>ModuleNotFoundError       | Модуль не найден                                                                                |
| * * <trd>LookupError                 | Проблемы с поиском                                                                              |
| * * * <fth>IndexError                | Пр.: не найден индекс                                                                           |
| * * * <fth>KeyError                  | Пр.: не найден ключ                                                                             |
| * * <trd>MemoryError                 | Проблемы с доступом к памяти                                                                    |
| * * <trd>NameError                   | Обращение к неизвестному имени (пр.: обращение к переменной до её присваивания)                 |
| * * * <fth>UnboundLocalError         |                                                                                                 |
| * * <trd>OSError                     | Ошибки при работе с ОС                                                                          |
| * * * <fth>BlockingIOError           |                                                                                                 |
| * * * <fth>ChildProcessError         |                                                                                                 |
| * * * <fth>ConnectionError           |                                                                                                 |
| * * * * <ffth>BrokenPipeError        |                                                                                                 |
| * * * * <ffth>ConnectionAbortedError |                                                                                                 |
| * * * * <ffth>ConnectionRefusedError |                                                                                                 |
| * * * * <ffth>ConnectionResetError   |                                                                                                 |
| * * * <fth>FileExistError            |                                                                                                 |
| * * * <fth>FileNotFoundError         |                                                                                                 |
| * * * <fth>InterruptedError          |                                                                                                 |
| * * * <fth>IsADirectoryError         |                                                                                                 |
| * * * <fth>NotADirectoryError        |                                                                                                 |
| * * * <fth>PermissionError           |                                                                                                 |
| * * * <fth>ProcessLookupError        |                                                                                                 |
| * * * <fth>TimeoutError              |                                                                                                 |
| * * <trd>ReferenceError              |                                                                                                 |
| * * <trd>RuntimeError                |                                                                                                 |
| * * * <fth>NotImplementedError       |                                                                                                 |
| * * * <fth>RecursionError            |                                                                                                 |
| * * <trd>StopAsyncIteration          | цикл for?                                                                                       |
| * * <trd>StopIteration               | цикл for?                                                                                       |
| * * <trd>SyntaxError                 |                                                                                                 |
| * * * <fth>IndentationError          |                                                                                                 |
| * * * * <ffth>TabError               | Ошибка табуляции                                                                                |
| * * <trd>SystemError                 | Непредвиденная ситуация в работе программы                                                      |
| * * <trd>TypeError                   | Ошибка типа: вызов метода/функции, отсутствующих у типа                                         |
| * * <trd>ValueError                  | Ошибка значения: операция со значением не может быть выполнена                                  |
| * * * <fth>UnicodeError              | Проблемы с кодировкой (пр.: строку в байты/байты в строку)                                      |
| * * * * <ffth>UnicodeDecodeError     |                                                                                                 |
| * * * * <ffth>UnicodeEncodeError     |                                                                                                 |
| * * * * <ffth>UnicodeTranslateError  |                                                                                                 |
| * * <trd>Warning                     | Предупреждения - программа не прекращает работу                                                 |
| * * * <fth>BytesWarning              |                                                                                                 |
| * * * <fth>DeprecationWarning        |                                                                                                 |
| * * * <fth>EncodingWarning           |                                                                                                 |
| * * * <fth>FutureWarning             |                                                                                                 |
| * * * <fth>ImportWarning             |                                                                                                 |
| * * * <fth>PendingDeprecationWarning |                                                                                                 |
| * * * <fth>ResourceWarning           |                                                                                                 |
| * * * <fth>RuntimeWarning            |                                                                                                 |
| * * * <fth>SyntaxWarning             |                                                                                                 |
| * * * <fth>UnicodeWarning            |                                                                                                 |
| * * * <fth>UserWarning               |                                                                                                 |

