import { PrismaClient } from "@prisma/client";

// Une seule instance de client, y compris en développement (rechargement à chaud).
const g = globalThis as unknown as { prisma?: PrismaClient };
export const db = g.prisma ?? new PrismaClient();
if (process.env.NODE_ENV !== "production") g.prisma = db;
