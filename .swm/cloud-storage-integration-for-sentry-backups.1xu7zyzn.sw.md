---
title: Cloud Storage Integration for Sentry Backups
---
<SwmSnippet path="/src/sentry/runner/commands/backup.py" line="42">

---

# Cloud Storage Integration for Backups

Sentry supports integration with Google Cloud's Key Management Service (KMS) for decrypting backup tarballs. This is facilitated through the `--decrypt-with-gcp-kms` flag, which allows the retrieval of keys directly from Google Cloud, thus avoiding the need to store private keys on the local machine.

```python
DECRYPT_WITH_GCP_KMS_HELP = """For users that want to avoid storing their own private keys, this
                            flag can be used in lieu of `--decrypt-with` to retrieve keys from
                            Google Cloud's Key Management Service directly, avoiding ever storing
                            them on the machine doing the decryption.

                            This flag should point to a JSON file containing a single top-level
                            object storing the `project-id`, `location`, `keyring`, `key`, and
                            `version` of the desired asymmetric private key that pairs with the
                            2048-bit public RSA key in text (PEM) format included in the tarball
                            being imported (for more information on these resource identifiers and
                            how to set up KMS to use the, see:
                            https://cloud.google.com/kms/docs/getting-resource-ids). An example
                            version of this file might look like:
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>
