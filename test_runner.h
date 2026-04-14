/*
 * Simple C test runner. Include this in any problem file.
 *
 * Usage:
 *   #include "../test_runner.h"
 *
 *   int solve(int* nums, int n, int target) {
 *       // your code here
 *   }
 *
 *   int main() {
 *       // use TEST_INT, TEST_ARR, TEST_BOOL, TEST_STR macros
 *   }
 */

#ifndef TEST_RUNNER_H
#define TEST_RUNNER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

static int _tr_passed = 0;
static int _tr_failed = 0;
static int _tr_total = 0;

/* Compare single int result */
#define TEST_INT(label, got, expected) do { \
    _tr_total++; \
    if ((got) == (expected)) { \
        _tr_passed++; \
        printf("  [%d] PASS  %s\n", _tr_total, label); \
    } else { \
        _tr_failed++; \
        printf("  [%d] FAIL  %s\n", _tr_total, label); \
        printf("         expected: %d\n", expected); \
        printf("         got:      %d\n", got); \
    } \
} while(0)

/* Compare float result (with epsilon) */
#define TEST_FLOAT(label, got, expected, eps) do { \
    _tr_total++; \
    double _diff = (got) - (expected); \
    if (_diff < 0) _diff = -_diff; \
    if (_diff < (eps)) { \
        _tr_passed++; \
        printf("  [%d] PASS  %s\n", _tr_total, label); \
    } else { \
        _tr_failed++; \
        printf("  [%d] FAIL  %s\n", _tr_total, label); \
        printf("         expected: %f\n", (double)(expected)); \
        printf("         got:      %f\n", (double)(got)); \
    } \
} while(0)

/* Compare bool result */
#define TEST_BOOL(label, got, expected) do { \
    _tr_total++; \
    if ((got) == (expected)) { \
        _tr_passed++; \
        printf("  [%d] PASS  %s\n", _tr_total, label); \
    } else { \
        _tr_failed++; \
        printf("  [%d] FAIL  %s\n", _tr_total, label); \
        printf("         expected: %s\n", (expected) ? "true" : "false"); \
        printf("         got:      %s\n", (got) ? "true" : "false"); \
    } \
} while(0)

/* Compare string result */
#define TEST_STR(label, got, expected) do { \
    _tr_total++; \
    if (strcmp((got), (expected)) == 0) { \
        _tr_passed++; \
        printf("  [%d] PASS  %s\n", _tr_total, label); \
    } else { \
        _tr_failed++; \
        printf("  [%d] FAIL  %s\n", _tr_total, label); \
        printf("         expected: \"%s\"\n", expected); \
        printf("         got:      \"%s\"\n", got); \
    } \
} while(0)

/* Compare array result */
#define TEST_ARR(label, got, expected, n) do { \
    _tr_total++; \
    int _match = 1; \
    for (int _i = 0; _i < (n); _i++) { \
        if ((got)[_i] != (expected)[_i]) { _match = 0; break; } \
    } \
    if (_match) { \
        _tr_passed++; \
        printf("  [%d] PASS  %s\n", _tr_total, label); \
    } else { \
        _tr_failed++; \
        printf("  [%d] FAIL  %s\n", _tr_total, label); \
        printf("         expected: ["); \
        for (int _i = 0; _i < (n); _i++) printf("%d%s", (expected)[_i], _i<(n)-1?",":""); \
        printf("]\n         got:      ["); \
        for (int _i = 0; _i < (n); _i++) printf("%d%s", (got)[_i], _i<(n)-1?",":""); \
        printf("]\n"); \
    } \
} while(0)

/* Print summary -- call at end of main */
#define TEST_SUMMARY() do { \
    printf("\n  %d/%d passed", _tr_passed, _tr_total); \
    if (_tr_failed) printf("  (%d failed)\n", _tr_failed); \
    else printf("  ok\n"); \
    return _tr_failed ? 1 : 0; \
} while(0)

/* Helper: make array literal inline */
#define ARR(...) (int[]){__VA_ARGS__}

#endif
