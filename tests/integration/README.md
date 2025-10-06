# Integration Tests

This directory contains simplified integration tests that hit the actual AniList GraphQL API endpoints to validate that the API client works correctly with real data.

## Test Structure

### Individual API Tests
- `test_anime_integration.py` - Two tests: `test_get_anime()` and `test_get_anime_by_id()`
- `test_manga_integration.py` - Two tests: `test_get_manga()` and `test_get_manga_by_id()`
- `test_character_integration.py` - Two tests: `test_get_character()` and `test_get_character_by_id()`
- `test_comprehensive_integration.py` - Combined tests covering all APIs
- `utils.py` - Reusable validation and utility functions

### Test Coverage
Each API test suite includes:
- One search test that validates list results and item structure
- One get-by-ID test that validates dictionary results
- Automatic 1-second delays between tests to respect API rate limits (45r/m)
- Comprehensive field validation using reusable utility functions

## Rate Limiting

⚠️ **Important**: AniList API has rate limiting (HTTP 429 responses) that will cause test failures when running many tests rapidly in sequence.

### Running Tests Safely

**Option 1: Run individual test files with delays**
```bash
python -m pytest tests/integration/test_anime_integration.py::TestAnimeIntegration::test_get_anime_rezero -v
# Wait a few seconds
python -m pytest tests/integration/test_manga_integration.py::TestMangaIntegration::test_get_manga_naruto -v
```

**Option 2: Run a single test at a time**
```bash
python -m pytest tests/integration/test_anime_integration.py::TestAnimeIntegration::test_get_anime_rezero -v
```

**Option 3: Use the test runner with delays**
```bash
python tests/integration/run_integration_tests.py
```

## Validation Functions

The `utils.py` module provides reusable validation functions:

- `validate_search_result()` - Validates list format and non-empty results
- `validate_anime_search_item()` - Validates individual anime items (id, title structure)
- `validate_manga_search_item()` - Validates individual manga items (id, title structure)  
- `validate_character_search_item()` - Validates individual character items (id, name)
- `validate_anime_by_id_result()` - Validates anime get-by-ID results (name fields)
- `validate_manga_by_id_result()` - Validates manga get-by-ID results (name fields)
- `validate_character_by_id_result()` - Validates character get-by-ID results (name fields)
- `rate_limit_delay()` - Adds 1-second delay to respect API rate limits

## Test Data Used

- **Anime**: Naruto (search), Naruto ID: 20 (get-by-ID)
- **Manga**: Death Note (search), Death Note ID: 30021 (get-by-ID)  
- **Character**: Luffy (search), Monkey D. Luffy ID: 40 (get-by-ID)

## Running Individual Tests

To avoid rate limiting, run tests individually:

```bash
# Test a single anime search
python -m pytest tests/integration/test_anime_integration.py::TestAnimeIntegration::test_get_anime_rezero -v

# Test a single character search
python -m pytest tests/integration/test_character_integration.py::TestCharacterIntegration::test_get_character_subaru -v

# Test get by ID functionality
python -m pytest tests/integration/test_anime_integration.py::TestAnimeIntegration::test_get_anime_by_id -v
```

## Expected Behavior

When rate limiting is not an issue, all tests should:
1. Return non-null results
2. Return non-empty lists for search operations
3. Return valid dictionaries for get-by-id operations
4. Have the expected field structure in returned data

## Summary

These simplified integration tests provide:
- ✅ Focused testing: Only 2 tests per API (search + get-by-ID)  
- ✅ Rate limiting protection: 1-second delays between tests
- ✅ Reusable validation: Common validation logic in utils.py
- ✅ Clear structure validation: Checks for correct data types and required fields
- ✅ Real API validation: Tests hit actual AniList endpoints to ensure functionality