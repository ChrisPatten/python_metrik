# Proof of Concept

This POC demonstrates offline execution of the schema loader utilities.

Run the entire flow with a single command:

```bash
make poc
```

The process completes in under ten seconds on a typical laptop and writes
results to `poc/output/`.

## Limitations

- No S3 or Snowflake connectivity is performed.
- Schema inference only supports CSV input files.
- Numeric type resolution uses a simple int/float heuristic.

## Next Steps

This demo is intentionally minimal. See project documentation for tasks
required for a full-scale implementation.
