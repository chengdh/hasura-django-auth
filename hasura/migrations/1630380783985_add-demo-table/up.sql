CREATE TABLE "public"."public_posts"(
 "id" serial NOT NULL,
 "title" text NOT NULL,
 "content" text NOT NULL,
 "created_at" timestamptz NOT NULL DEFAULT now(),
 "updated_at" timestamptz NOT NULL DEFAULT now(),
 "created_by" integer NOT NULL,
 PRIMARY KEY ("id")
 );