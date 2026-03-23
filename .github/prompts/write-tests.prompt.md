# Write Unit Tests (pytest)

Generate unit tests for the following code using `pytest`:

1. **Test structure**:
   ```python
   def test_<function>_<scenario>():
       # Arrange
       input_data = ...
       
       # Act
       result = function(input_data)
       
       # Assert
       assert result == expected
   ```

2. **Coverage**:
   - Happy path (valid inputs)
   - Edge cases (empty, None, boundary values)
   - Error cases (invalid inputs, exceptions)

3. **Fixtures** for reusable setup:
   ```python
   @pytest.fixture
   def sample_data():
       return {...}
   ```

4. **Mocking** external dependencies (DB, API calls):
   ```python
   from unittest.mock import patch
   @patch('module.external_function')
   def test_with_mock(mock_func):
       ...
   ```

5. **Parametrization** for multiple inputs:
   ```python
   @pytest.mark.parametrize("input,expected", [...])
   def test_multiple(input, expected):
       ...
   ```

Ensure tests are concise and focused on one thing per test.

Reference standards: See .github/copilot-instructions.md

